<?php

declare(strict_types=1);

//Basic.
echo file_get_contents('https://jsonplaceholder.typicode.com/todos/1');

//Use class. (curl)
try {
    echo (new crudHttp('https://jsonplaceholder.typicode.com'))->requestGet('/todos/1');
} catch (Throwable $exception) {
    echo "Exception[".$exception->getCode()."]: ".$exception->getMessage();
}

class crudHttp
{
    private const REQUEST_TYPE_GET = 'GET';
    private const REQUEST_TYPE_POST = 'POST';
    private const REQUEST_TYPE_PUT = 'PUT';
    private const REQUEST_TYPE_DELETE = 'DELETE';
    private ?string $baseUri;
    private int $timeOut;

    public function __construct(?string $baseUri = null, ?int $timeOut = null)
    {
        $this->baseUri = $baseUri ? trim($baseUri) : $baseUri;
        $this->timeOut = $timeOut ?? 0;
    }

    /**
     * @param string $endpoint
     * @param array $headers
     *
     * @return string
     * @throws Exception
     */
    public function requestGet(string $endpoint, array $headers = []): string
    {
        return $this->request(self::REQUEST_TYPE_GET, $endpoint, $headers);
    }

    /**
     * @param string $endpoint
     * @param array $headers
     * @param string|null $body
     *
     * @return string
     * @throws Exception
     */
    public function requestPost(string $endpoint, array $headers = [], ?string $body = null): string
    {
        return $this->request(self::REQUEST_TYPE_POST, $endpoint, $headers, $body);
    }

    /**
     * @param string $endpoint
     * @param array $headers
     * @param string|null $body
     *
     * @return string
     * @throws Exception
     */
    public function requestPut(string $endpoint, array $headers = [], ?string $body = null): string
    {
        return $this->request(self::REQUEST_TYPE_PUT, $endpoint, $headers, $body);
    }

    /**
     * @param string $endpoint
     * @param array $headers
     *
     * @return string
     * @throws Exception
     */
    public function requestDelete(string $endpoint, array $headers = []): string
    {
        return $this->request(self::REQUEST_TYPE_DELETE, $endpoint, $headers);
    }

    /**
     * @param string $type
     * @param string $endpoint
     * @param array $headers
     * @param string|null $body
     *
     * @return string
     * @throws Exception
     */
    private function request(string $type, string $endpoint, array $headers, ?string $body = null): string
    {
        $uri = $this->baseUri ? $this->baseUri.$endpoint : $endpoint;

        $options = [
            CURLOPT_URL => $uri,
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_TIMEOUT => $this->timeOut,
            CURLOPT_FOLLOWLOCATION => true,
            CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
            CURLOPT_CUSTOMREQUEST => $type,
            CURLOPT_POSTFIELDS => $body,
            CURLOPT_HTTPHEADER => $headers,
        ];

        $curl = curl_init();

        curl_setopt_array($curl, $options);

        $bodyResult = curl_exec($curl);

        $this->validateStatusCode(curl_getinfo($curl, CURLINFO_HTTP_CODE));

        curl_close($curl);

        return $bodyResult;
    }

    /**
     * @param int $status
     *
     * @return void
     * @throws Exception
     */
    private function validateStatusCode(int $status): void
    {
        if ($status >= 200 && $status < 300) {
            return;
        }

        throw new Exception('Unexpected HTTP code: '.$status, $status);
    }
}